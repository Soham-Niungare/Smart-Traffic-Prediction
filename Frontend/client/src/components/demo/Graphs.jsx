import { Chart1 } from "./ChartDemo1";
import { Chart2 } from "./ChartDemo2";
import { Chart3 } from "./ChartDemo3";
import { Chart4 } from "./ChartDemo4";

const chartData = [
  { month: "January", desktop: 186, mobile: 80 },
  { month: "February", desktop: 305, mobile: 200 },
  { month: "March", desktop: 237, mobile: 120 },
  { month: "April", desktop: 730, mobile: 190 },
  { month: "May", desktop: 209, mobile: 130 },
  { month: "June", desktop: 214, mobile: 140 },
];

export function Graphs() {
  return (
    <>
      <div className="grid grid-cols-1 gap-4 my-4 mx-4 lg:grid-cols-2 lg:gap-8">
        <Chart1 chartData={chartData} />
        <Chart2 chartData={chartData} />
        <Chart3 />
        <Chart4 chartData={chartData} />
      </div>
    </>
  );
}
