package com.HF.component;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class MyClient {
    private String host;
    private int port;

    public MyClient(String h, int p) {
        host = h;
        port = p;
    }

    public void start() {
        try {
            try (Socket socket = new Socket(host, port)) {
                System.out.println("Connected");
                try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                        PrintWriter out = new PrintWriter(socket.getOutputStream());
                        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in))) {

                    Thread sendThread = new Thread(() -> {
                        try {
                            String message;
                            boolean running = true;
                            while (running) {
                                message = stdIn.readLine();
                                if (message != null) {
                                    out.println(message);
                                    out.flush();
                                    if (message.equals("bye")) {
                                        running = false;
                                    }
                                }
                            }
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    });

                    Thread receiveThread = new Thread(() -> {
                        try {
                            String message;
                            while ((message = in.readLine()) != null) {
                                System.out.println("The Client has received the message from the Server: " + message);
                            }
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    });

                    sendThread.start();
                    receiveThread.start();

                    sendThread.join();
                    receiveThread.join();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
