package raspberryPiCode;

import gnu.io.CommPort;
import gnu.io.CommPortIdentifier;
import gnu.io.SerialPort;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class TwoWaySerialComm {

	SerialReader reader;
	SerialWriter writer;

	void write(String message) {
		writer.writeLine(message);
	}
	
	String read() {
		return reader.readLine();
	}
	
	void connect(String portName) throws Exception {
		CommPortIdentifier portIdentifier = CommPortIdentifier
				.getPortIdentifier(portName);
		if (portIdentifier.isCurrentlyOwned()) {
			System.out.println("Error: Port is currently in use");
		} else {
			int timeout = 2000;
			CommPort commPort = portIdentifier.open(this.getClass().getName(),
					timeout);

			if (commPort instanceof SerialPort) {
				SerialPort serialPort = (SerialPort) commPort;
				serialPort.setSerialPortParams(57600, SerialPort.DATABITS_8,
						SerialPort.STOPBITS_1, SerialPort.PARITY_NONE);

				InputStream in = serialPort.getInputStream();
				OutputStream out = serialPort.getOutputStream();

				reader = new SerialReader(in);
				writer = new SerialWriter(out);

			} else {
				System.out
						.println("Error: Only serial ports are handled by this example.");
			}
		}
	}

	public static class SerialReader {

		InputStream in;

		public SerialReader(InputStream in) {
			this.in = in;
		}

		public String readLine() {
			byte[] buffer = new byte[1024];
			int len = -1;
			StringBuilder builder = new StringBuilder();

			try {
				while ((len = this.in.read(buffer)) != -1) {
					builder.append(new String(buffer, 0, len));
				}
			} catch (IOException e) {
				e.printStackTrace();
			}

			return builder.toString();
		}
	}

	public static class SerialWriter {

		OutputStream out;

		public SerialWriter(OutputStream out) {
			this.out = out;
		}

		public void writeLine(String message) {
			byte[] bytes = message.getBytes();

			try {
				this.out.write(bytes);
				this.out.flush();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

	public static void main(String[] args) {
		try {
			TwoWaySerialComm comm = new TwoWaySerialComm();
			comm.connect("/dev/ttyACM0");
			System.out.println("Writing to comm: gl\\n");
			comm.write("gl\n");
			try {
			    Thread.sleep(1000);               
			} catch(InterruptedException ex) {
			    Thread.currentThread().interrupt();
			}
			System.out.println("Read from comm: " + comm.read());
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}