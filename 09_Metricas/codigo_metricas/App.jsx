import { useState } from "react";
import Login from "./components/Login";
import Chat from "./components/Chat";
import "./styles/Login.css"; // Importar estilos


const App = () => {
    const [username, setUsername] = useState(null);

    return (
        <div>
            {username ? <Chat username={username} setUsername={setUsername} /> : <Login setUsername={setUsername} />}
        </div>
    );
};

export default App;
