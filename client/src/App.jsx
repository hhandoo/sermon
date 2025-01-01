import React, { useState } from "react";
import { Container, Switch, Typography, Paper } from "@mui/material";
import { Grid2 } from "@mui/material";

const appliances = [
  "Router",
  "8 Port Switch",
  "Undefined 2",
  "Undefined 3",
  "Undefined 4",
  "Undefined 5",
  "Undefined 6",
  "Undefined 7",
];

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

  return (
    <Container style={{ marginTop: "20px" }}>
      <Typography variant="h4" align="center" gutterBottom>
        Sermon Appliance Controller v1.0
      </Typography>
      <Grid2 container={true} spacing={4}>
        {appliances.map((appliance) => (
          <Grid2 size={{ xs: 12, md: 4, sm: 6 }} key={appliance}>
            <Paper
              elevation={8}
              style={{ padding: "16px", textAlign: "center" }}
            >
              <Typography variant="h6"  gutterBottom>
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
