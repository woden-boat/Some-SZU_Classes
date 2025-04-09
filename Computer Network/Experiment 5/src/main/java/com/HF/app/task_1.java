package com.HF.app;

import java.net.InetAddress;
import java.net.UnknownHostException;
import com.HF.component.Downloader;

public class task_1 {
    public static void main(String[] args) {
        try {
            InetAddress localAddress = InetAddress.getLocalHost();
            System.out.println("Local Host Name: " + localAddress.getHostName());
            System.out.println("Local Host IP: " + localAddress.getHostAddress());

            InetAddress csdnAddress = InetAddress.getByName("www.csdn.net");
            System.out.println("CSDN Host IP: " + csdnAddress.getHostAddress());

            String s = "https://www.szu.edu.cn";
            Downloader dl = new Downloader(s);
            String savePath = "E:\\SZU_Classes\\My_Classes\\Computer Network\\Experiment 5\\result";
            dl.Save(savePath);
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}
