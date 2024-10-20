import { Input } from "@/components/ui/input";
import { DropdownMenuLoc } from "./DropdownLoc";
import { DropdownMenuWeather } from "./DropdownMenuWeather";
import { CalendarDemo } from "./CalendarDemo";
import { Button } from "../ui/button";
import { useState } from "react";

export function InputDemo(props) {
  const [selectedDate, setSelectedDate] = useState(null);
  const [selectedLocation, setSelectedLocation] = useState(null);
  const [selectedWeather, setSelectedWeather] = useState(null);
  const [showPrediction, setShowPrediction] = useState(false);

  const handleLocationChange = (location) => {
    setSelectedLocation(location);
  };

  const handleWeatherChange = (weather) => {
    setSelectedWeather(weather);
  };

  const handleDateChange = (formattedDate) => {
    setSelectedDate(formattedDate);
  };

  const handleSubmit = () => {
    console.log("Selected Location:", selectedLocation);
    console.log("Selected Date:", selectedDate);
    console.log("Selected Weather:", selectedWeather);
    setShowPrediction(true);
  };

  const handleClear = () => {
    setSelectedLocation(null);
    setSelectedDate(null);
    setSelectedWeather(null);
    setShowPrediction(false);
  };

  return (
    <>
      <div className="flex flex-col gap-16 bg-gray-800 rounded-3xl py-20 shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]">
        <div className="flex flex-col text-center">
          <span className="font-bold text-4xl text-center text-white">
            Enter Your{" "}
            <span className="bg-gradient-to-bl from-blue-500 to-blue-800 bg-clip-text text-transparent">
              Route,
            </span>
          </span>
          <span className="font-bold text-6xl text-center text-white">
            <span className="bg-gradient-to-bl from-blue-500 to-blue-800 bg-clip-text text-transparent">
              Predict
            </span>{" "}
            the Future
          </span>
        </div>

        <div className="flex flex-wrap justify-evenly items-center sm:flex-row">
          <div className="flex w-[80%] sm:w-[20%]">
            <Input
              type="text"
              placeholder={
                selectedLocation ? selectedLocation : "Select Location"
              }
              className="rounded-tl-2xl rounded-bl-2xl text-black bg-white shadow-[0_3px_10px_rgb(0,0,0,0.2)] border border-gray-200"
            />
            <DropdownMenuLoc
              roadNames={props.roadNames}
              onLocationChange={handleLocationChange}
            />
          </div>
          <CalendarDemo onDateChange={handleDateChange} />
          <div className="flex w-[80%] sm:w-[20%]">
            <Input
              type="text"
              placeholder={selectedWeather ? selectedWeather : "Select Weather"}
              className="rounded-tl-2xl rounded-bl-2xl text-black bg-white shadow-[0_3px_10px_rgb(0,0,0,0.2)] border border-gray-200"
            />
            <DropdownMenuWeather onWeatherChange={handleWeatherChange} />
          </div>
        </div>
        <div className="flex flex-row gap-4 justify-center">
          <Button
            className="w-[200px] text-lg font-semibold rounded-2xl px-4 py-2 bg-white hover:bg-gray-800 text-gray-800 hover:text-white border border-gray-200 shadow-[rgba(0,_0,_0,_0.4)_0px_30px_90px]"
            onClick={handleSubmit}
          >
            Predict
          </Button>
          <Button
            className="w-[200px] text-lg font-semibold rounded-2xl px-4 py-2 bg-red-500 hover:bg-red-700 hover:text-white text-gray-800 shadow-[rgba(0,_0,_0,_0.4)_0px_30px_90px]"
            onClick={handleClear}
          >
            Clear Prediction
          </Button>
        </div>
        {showPrediction && (
          <div
            id="Prediction"
            className="text-2xl font-semibold text-white text-center"
          >
            Prediction: 72.5% Traffic
          </div>
        )}
      </div>
    </>
  );
}
