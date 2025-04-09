package com.HF.app;

import com.HF.component.MyClient;

public class task_2_client {
    public static void main(String[] args) {
        MyClient client = new MyClient("localhost", 8888);

        client.start();
    }
}
