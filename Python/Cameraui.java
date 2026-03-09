import javax.swing.*;
import java.awt.event.*;
import java.io.IOException;

public class Cameraui {

    public static void main(String[] args) {

        JFrame frame = new JFrame("Face Recognition Attendance");
        JButton startCamera = new JButton("Start Camera");

        startCamera.setBounds(120,100,150,40);

        startCamera.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {

                try {
                    ProcessBuilder pb = new ProcessBuilder(
                        "py","-3.10","camera.py"
                    );
                    pb.start();
                } catch (IOException ex) {
                    ex.printStackTrace();
                }

            }
        });

        frame.add(startCamera);
        frame.setSize(400,300);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}