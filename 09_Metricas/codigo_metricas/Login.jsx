import { useState } from "react";
import { FaUser } from "react-icons/fa";

const Login = ({ setUsername }) => {
    const [name, setName] = useState("");
    const [error, setError] = useState("");

    const handleJoin = () => {
        if (name.trim() === "") {
            setError("El nombre de usuario es obligatorio");
            return;
        }
        setError("");
        setUsername(name);
    };

    const handleKeyPress = (e) => {
        if (e.key === "Enter") {
            handleJoin();
        }
    };

    return (
        <div className="login-container">
            <div className="login-card">
                <h2>Bienvenido al Chat</h2>
                <div className="input-container">
                    <FaUser className="icon" />
                    <input
                        type="text"
                        placeholder="Ingresa tu nombre"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        onKeyDown={handleKeyPress}
                    />
                </div>
                {error && <p className="error-message">{error}</p>}
                <button onClick={handleJoin}>Entrar</button>
            </div>
        </div>
    );
};

export default Login;
