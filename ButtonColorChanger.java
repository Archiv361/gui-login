import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class ButtonColorChanger extends JFrame {
    private JButton[] buttons = new JButton[6];
    private Color[] colors = {Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.MAGENTA, Color.CYAN};
    private String[] colorNames = {"Red", "Green", "Blue", "Yellow", "Magenta", "Cyan"};

    public ButtonColorChanger() {
        setTitle("BG Changer");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setBackground(Color.WHITE);
        setLayout(new GridBagLayout());

        setSize(800, 600);

        final JPanel buttonsPanel = new JPanel(new GridLayout(1, 6, 1, 5));
        buttonsPanel.setBackground(Color.WHITE);
        buttonsPanel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));

        for (int i = 0; i < 6; i++) {
            buttons[i] = new JButton(colorNames[i]);
            buttons[i].setFont(new Font("Arial", Font.BOLD, 12));
            buttons[i].setPreferredSize(new Dimension(80, 30));

            buttons[i].setBackground(Color.WHITE);
            buttons[i].setOpaque(true);
            buttons[i].setBorderPainted(false);
            buttons[i].setForeground(Color.BLACK);

            final int buttonIndex = i;
            buttons[i].addActionListener(e -> {
                Color selectedColor = colors[buttonIndex];
                getContentPane().setBackground(selectedColor);
                buttonsPanel.setBackground(selectedColor);
            });
            
            buttonsPanel.add(buttons[i]);
        }

        JPanel centerPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 0, 0));
        centerPanel.add(buttonsPanel);
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        gbc.anchor = GridBagConstraints.CENTER;
        add(centerPanel, gbc);

        setVisible(true);
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ButtonColorChanger());
    }
}
