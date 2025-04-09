package com.HF.component;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;

public class Downloader {
    private URL url;

    public Downloader(String s) {
        try {
            url = new URL(s);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
    }

    public void Save(String s) {

        try {

            try (InputStream in = url.openStream();
                    FileOutputStream fout = new FileOutputStream(new File(s + "\\szu.html"))) {
                byte[] buffer = new byte[1024];
                int byteRead;
                long totalBytes = 0;

                while ((byteRead = in.read(buffer)) != -1) {
                    fout.write(buffer, 0, byteRead);
                    totalBytes += byteRead;
                }

                System.out.println("The Size of File: " + totalBytes);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
