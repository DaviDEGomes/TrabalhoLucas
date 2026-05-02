import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class ChatUI extends JFrame {

    JTextArea chatArea;
    JTextField inputField;

    public ChatUI() {
        setTitle("AI Chat");
        setSize(900, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // FUNDO
        JPanel background = new JPanel();
        background.setBackground(new Color(15, 10, 30));
        background.setLayout(new GridBagLayout());

        // CONTAINER PRINCIPAL (vertical)
        JPanel container = new JPanel();
        container.setOpaque(false);
        container.setLayout(new BoxLayout(container, BoxLayout.Y_AXIS));

        // 🔹 TÍTULO GRANDE
        JLabel title = new JLabel("MovieAI");
        title.setForeground(Color.WHITE);
        title.setFont(new Font("Segoe UI", Font.BOLD, 40));
        title.setAlignmentX(Component.CENTER_ALIGNMENT);

        container.add(title);
        container.add(Box.createRigidArea(new Dimension(0, 20)));

        // 🔹 CARD
        JPanel card = new JPanel();
        card.setPreferredSize(new Dimension(500, 300));
        card.setBackground(new Color(40, 20, 70));
        card.setLayout(new BorderLayout());
        card.setBorder(BorderFactory.createEmptyBorder(15,15,15,15));

        // 🔹 "ABA" (simulação)
        JPanel tabPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        tabPanel.setOpaque(false);

        JLabel chatTab = new JLabel("Chat");
        chatTab.setForeground(Color.WHITE);
        chatTab.setFont(new Font("Segoe UI", Font.BOLD, 14));

        tabPanel.add(chatTab);

        // 🔹 CHAT AREA
        chatArea = new JTextArea();
        chatArea.setEditable(false);
        chatArea.setBackground(new Color(60, 30, 100));
        chatArea.setForeground(Color.WHITE);
        chatArea.setFont(new Font("Segoe UI", Font.PLAIN, 13));

        JScrollPane scroll = new JScrollPane(chatArea);
        scroll.setBorder(null);

        // 🔹 INPUT + BOTÃO
        JPanel inputPanel = new JPanel(new BorderLayout(10,0));
        inputPanel.setOpaque(false);

        inputField = new JTextField();
        inputField.setBackground(new Color(80, 40, 130));
        inputField.setForeground(Color.WHITE);
        inputField.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));

        JButton sendButton = new JButton("Enviar");
        sendButton.setBackground(new Color(120, 60, 200));
        sendButton.setForeground(Color.WHITE);
        sendButton.setFocusPainted(false);

        sendButton.addActionListener(e -> enviarMensagem());
        inputField.addActionListener(e -> enviarMensagem());

        inputPanel.add(inputField, BorderLayout.CENTER);
        inputPanel.add(sendButton, BorderLayout.EAST);

        // ADD NO CARD
        card.add(tabPanel, BorderLayout.NORTH);
        card.add(scroll, BorderLayout.CENTER);
        card.add(inputPanel, BorderLayout.SOUTH);

        container.add(card);

        background.add(container);
        setContentPane(background);

        setVisible(true);
    }

    private void enviarMensagem() {
        String texto = inputField.getText();
        if (texto.isEmpty()) return;

        chatArea.append("Você: " + texto + "\n");

        try {
            ProcessBuilder pb = new ProcessBuilder("python", "recomendador.py", texto);
            pb.redirectErrorStream(true);
            Process p = pb.start();

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(p.getInputStream())
            );

            String linha;
            chatArea.append("Bot:\n");
            while ((linha = reader.readLine()) != null) {
                chatArea.append("  - " + linha + "\n");
            }

        } catch (Exception ex) {
            chatArea.append("Erro ao chamar Python\n");
        }

        inputField.setText("");
    }

    public static void main(String[] args) {
        new ChatUI();
    }
}