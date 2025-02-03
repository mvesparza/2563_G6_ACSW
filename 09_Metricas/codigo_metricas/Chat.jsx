import { useEffect, useState, useRef } from "react";

const Chat = ({ username, setUsername }) => {
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState("");
    const [systemMessages, setSystemMessages] = useState([]);
    const [ws, setWs] = useState(null);
    const [serverError, setServerError] = useState(false);
    const chatBoxRef = useRef(null);

    useEffect(() => {
        const websocket = new WebSocket("ws://10.40.34.192:8082/chat");

        websocket.onopen = () => {
            setWs(websocket);
            setServerError(false);
            websocket.send(username);
        };

        websocket.onerror = () => {
            setServerError(true);
        };

        websocket.onmessage = (event) => {
            const msg = event.data;
            const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

            if (msg.includes("se ha unido al chat") || msg.includes("ha abandonado el chat")) {
                setSystemMessages((prev) => [...prev, { text: msg, time: timestamp }]);
            } else {
                // Evitar duplicados: Solo añadir si no existe el mensaje
                setMessages((prev) => {
                    if (!prev.some(m => m.text === msg && m.time === timestamp)) {
                        return [...prev, { text: msg, sender: msg.startsWith(username), time: timestamp }];
                    }
                    return prev;
                });
            }

            scrollToBottom();
        };

        return () => websocket.close();
    }, [username]);

    const sendMessage = () => {
        if (message.trim() !== "" && ws) {
            ws.send(message); // Enviar mensaje al WebSocket
            setMessage("");   // Limpiar input
            scrollToBottom();
        }
    };

    const leaveChat = () => {
        setUsername(null);
        ws.close();
    };

    const scrollToBottom = () => {
        setTimeout(() => {
            if (chatBoxRef.current) {
                chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
            }
        }, 100);
    };

    return (
        <div className="chat-container">
            {serverError && <div className="server-error">No hay sesiones disponibles</div>}

            {/* Mensajes del sistema */}
            <div className="chat-sidebar">
                <h3>Actividad</h3>
                {systemMessages.map((msg, index) => (
                    <div key={index} className="system-message">
                        {msg.text} <span className="timestamp">{msg.time}</span>
                    </div>
                ))}
            </div>

            {/* Chat principal */}
            <div className="chat-main">
                <div className="chat-header">Chat en Vivo</div>
                <div className="chat-box" ref={chatBoxRef}>
                    {messages.map((msg, index) => (
                        <div key={index} className={msg.sender ? "user-message" : "other-message"}>
                            {msg.text}
                            <span className="timestamp">{msg.time}</span>
                        </div>
                    ))}
                </div>

                {/* Entrada de mensaje */}
                <div className="chat-input">
                    <input
                        type="text"
                        placeholder="Escribe un mensaje..."
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
                    />
                    <button className="enviar" onClick={sendMessage}>Enviar</button>
                    <button className="exit" onClick={leaveChat}>Salir</button>
                </div>
            </div>
        </div>
    );
};

export default Chat;
