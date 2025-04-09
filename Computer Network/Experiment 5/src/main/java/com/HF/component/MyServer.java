package com.HF.component;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class MyServer {
    private int port = 8888;

    public void start() {
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("The Server has been started...");
            while (true) {
                try (Socket clientSocket = serverSocket.accept()) { // 使用 try-with-resources 管理 Socket
                    System.out.println("The Client is connected");
                    System.out.println("Client Host Name: " + clientSocket.getInetAddress().getHostName());
                    System.out.println("Client Host Address: " + clientSocket.getInetAddress().getHostAddress());

                    // 使用 try-with-resources 管理 BufferedReader 和 PrintWriter
                    try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                        String message;
                        while ((message = in.readLine()) != null) {
                            System.out.println("The message from Client: " + message);

                            if (message.equals("time")) { // 使用 equals 比较字符串
                                LocalDateTime now = LocalDateTime.now();
                                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
                                String formattedTime = now.format(formatter);

                                out.println(formattedTime);
                            } else if (message.equals("bye")) {
                                System.out.println("disconnected...");
                                break;
                            } else {
                                out.println("The Sever has received the message from the Client: " + message);
                            }
                        }
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
