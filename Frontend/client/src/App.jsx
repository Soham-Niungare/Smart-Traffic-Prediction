import { useEffect, useState } from "react";
import axios from "axios";
import { Navbar } from "./components/demo/Navbar";
import { Graphs } from "./components/demo/Graphs";

function App() {
  const [array, setArray] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://127.0.0.1:8080/api/users");
    setArray(response.data.users);
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      <div className="w-full  flex flex-col gap-4 bg-gray-200">
        <Navbar />
        {/* <div>
          {array.map((user, index) => (
            <div key={index} className="font-semibold text-lg">
              <span>{user}</span>
            </div>
          ))}
        </div> */}
        <section>
          <Graphs />
        </section>
      </div>
    </>
  );
}

export default App;
