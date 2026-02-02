import { useEffect, useState } from "react";

function App() {
  const [keypad, setKeypad] = useState(null);
  const [tokens, setTokens] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/keypad/init", { method: "POST" })
      .then((res) => res.json())
      .then((data) => setKeypad(data))
      .catch(console.error);
  }, []);

  if (!keypad) return <div>Loading keypad...</div>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Secure Keypad (ver.1.0.0)</h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, 80px)",
          gap: 10,
          marginTop: 20,
        }}
      >
        {keypad.layout.map((key, i) => (
          <button
            key={i}
            //disabled={key.type === "empty"}
            style={{
              height: 80,
              opacity: key.type === "empty" ? 0.3 : 1,
              cursor: key.type === "empty" ? "default" : "pointer",
            }}
            onClick={() => {
              if (key.type === "number") {
                setTokens((prev) => [...prev, key.token]);
                console.log("number token:", key.token);
              } else {
                // 🔑 empty 클릭 시 빈 문자열 저장
                setTokens((prev) => [...prev, ""]);
                console.log("empty token: (empty string)");
              }
            }}
          >
            <img
              src={`http://127.0.0.1:8000${key.image}`}
              alt=""
              draggable={false}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",   // 🔑 꽉 차게 (비율 유지)
                pointerEvents: "none",
                display: "block",     // 🔑 하단 공백 제거
              }}
            />
          </button>
        ))}
      </div>

      <pre style={{ marginTop: 20 }}>
        {tokens.map((t, i) => (
          <div key={i}>
            [{i}] {t === "" ? "(empty)" : t}
          </div>
        ))}
      </pre>
    </div>
  );
}

export default App;
