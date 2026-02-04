import { useEffect, useState } from "react";

function App() {
  const [keypadData, setKeypadData] = useState(null);
  const [inputValues, setInputValues] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/keypad/init", { method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        setKeypadData(data);
      })
      .catch(console.error);
  }, []);

  if (!keypadData || !keypadData.layout) return <div>Loading keypad...</div>;

  return (
    <div style={{ padding: 20, fontFamily: "sans-serif" }}>
      <h2>Secure Keypad (ver.1.0.2)</h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 80px)",
          gap: 10,
          marginTop: 30,
        }}
      >
        {keypadData.layout.map((key) => (
          <button
            key={key.id}
            style={{
              height: 80,
              width: 80,
              padding: 0,
              border: "1px solid #ddd",
              borderRadius: "8px",
              backgroundColor: "#fff",
              
              /* ✅ 수정됨: Empty 버튼도 항상 보이게 설정 (opacity: 1) */
              opacity: 1, 
              
              /* ✅ UX: Empty 버튼은 클릭 안 된다는 느낌을 주기 위해 커서 설정 */
              cursor: key.type === "empty" ? "default" : "pointer",
              
              /* ✅ 선택사항: Empty 버튼 클릭 자체를 막고 싶다면 none, 
                 눌리는 느낌(hover 등)을 주고 싶다면 auto로 하세요. 
                 여기서는 클릭해도 값만 안 들어가게 하기 위해 auto로 둡니다. */
              pointerEvents: key.type === "empty" ? "none" : "auto",
              
              overflow: "hidden",
            }}
            onClick={() => {
              // type이 number일 때만 입력값에 추가
              if (key.type === "number") {
                setInputValues((prev) => [...prev, key.value]);
              }
            }}
          >
            <img
              src={key.image}
              alt={key.value}
              draggable={false}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "fill", // 이미지 꽉 채우기
                display: "block",
              }}
            />
          </button>
        ))}
      </div>

      <div 
        style={{ 
          marginTop: 30, 
          padding: "15px", 
          background: "#222",
          color: "rgb(215, 255, 215)",
          borderRadius: "8px",
          fontSize: "1.2rem",
          fontWeight: "bold",
          letterSpacing: "2px"
        }}
      >
        <div>Input Debug:</div>
        <div style={{ marginTop: "10px", wordBreak: "break-all" }}>
          {inputValues.length > 0 ? inputValues.join(" ") : "(입력 대기 중...)"}
        </div>
      </div>
    </div>
  );
}

export default App;