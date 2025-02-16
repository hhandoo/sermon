import React, { useState } from "react";
import {
  Container,
  Switch,
  Typography,
  Paper,
  TextField,
  Button,
  Box,
} from "@mui/material";
import { Grid2 } from "@mui/material";

const appliances = ["Undefined 1", "Undefined 2", "GX Router", "8 Port Switch"];

function App() {
  const [applianceStates, setApplianceStates] = useState(
    appliances.reduce((state, appliance) => {
      state[appliance] = false;
      return state;
    }, {})
  );

  const handleToggle = (appliance) => {
    setApplianceStates((prevState) => ({
      ...prevState,
      [appliance]: !prevState[appliance],
    }));
  };
  const [command, setCommand] = useState("");

  const handleSendCommand = () => {
    if (command.length === appliances.length && /^[01]+$/.test(command)) {
      const newStates = appliances.reduce((state, appliance, index) => {
        state[appliance] = command[index] === "1";
        return state;
      }, {});
      setApplianceStates(newStates);
    } else {
    }
  };
  return (
    <Container style={{ marginTop: "20px" }}>
      <Typography variant="h4" align="center" gutterBottom>
        Sermon Appliance Controller v1.0
      </Typography>
      <TextField
        label="Enter Command (e.g., 1100)"
        variant="outlined"
        value={command}
        onChange={(e) => setCommand(e.target.value)}
        fullWidth
        margin="normal"
      />
      <Box display="flex" justifyContent="center" marginTop={2}>
        <Button variant="contained" color="primary" onClick={handleSendCommand}>
          Send Command
        </Button>
      </Box>
      <Grid2 container={true} spacing={4} sx={{ mt: 4 }}>
        {appliances.map((appliance) => (
          <Grid2 size={{ xs: 12, md: 4, sm: 6 }} key={appliance}>
            <Paper
              elevation={2}
              style={{
                padding: "16px",
                textAlign: "center",
                borderRadius: "10px",
              }}
            >
              <Typography variant="h6" gutterBottom>
                {appliance}
              </Typography>
              <Switch
                checked={applianceStates[appliance]}
                onChange={() => handleToggle(appliance)}
                color="primary"
              />
              <Typography variant="body1">
                {applianceStates[appliance] ? "ON" : "OFF"}
              </Typography>
            </Paper>
          </Grid2>
        ))}
      </Grid2>
    </Container>
  );
}

export default App;
