async function generateResume() {
    const name = document.getElementById("name").value;
    const position = document.getElementById("position").value;

    const response = await fetch("http://localhost:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, position })
    });

    const data = await response.json();
    document.getElementById("resume").innerText = data.resume;
}
