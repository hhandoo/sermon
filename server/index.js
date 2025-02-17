const express = require("express");
const bodyParser = require("body-parser");
const { exec } = require("child_process");

const app = express();
const PORT = 3001;

app.use(bodyParser.json());

app.post("/send-command", (req, res) => {
  const { input } = req.body;

  if (!/^[01]+$/.test(input)) {
    return res
      .status(400)
      .json({ error: "Invalid input, only binary strings allowed" });
  }

  exec(`./script.sh ${input}`, (error, stdout, stderr) => {
    if (error) {
      return res
        .status(500)
        .json({ error: stderr || "Error executing script" });
    }
    res.json({
      message: "Script executed successfully",
      output: stdout.trim(),
    });
  });
});

// Simple GET request
app.get("/get-all-states", (req, res) => {
  res.send("Node.js Server is Running!");
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
