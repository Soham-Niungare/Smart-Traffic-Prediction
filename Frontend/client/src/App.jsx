import React, { useState, useEffect } from "react";
import axios from "axios";
import { Navbar } from "./components/demo/Navbar";
import { Graphs } from "./components/demo/Graphs";
import { InputDemo } from "./components/demo/InputDemo";

function App() {
  const [roadNames, setRoadNames] = useState([]);

  useEffect(() => {
    const fetchRoadNames = async () => {
      const response = await axios.get("http://127.0.0.1:8080/api/road_names");
      setRoadNames(response.data.road_names);
    };

    fetchRoadNames();
  }, []);

  return (
    <div className="w-full  flex flex-col gap-4 bg-gray-200">
      <Navbar />
      <InputDemo roadNames={roadNames} />
      <section>
        <Graphs />
      </section>
    </div>
  );
}

export default App;
