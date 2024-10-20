import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { IoIosArrowDropdown } from "react-icons/io";

export function DropdownMenuWeather({ onWeatherChange }) {
  const handleSelect = (weather) => {
    onWeatherChange(weather);
  };
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button
          variant="outline"
          className="rounded-tr-2xl rounded-br-2xl bg-white text-gray-800 hover:text-white hover:bg-gray-800 border border-gray-200 text-lg shadow-[0_3px_10px_rgb(0,0,0,0.2)]"
        >
          <IoIosArrowDropdown></IoIosArrowDropdown>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56 bg-white text-black overflow-y-auto max-h-60">
        <DropdownMenuLabel>Menu</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuGroup>
          <DropdownMenuItem
            onClick={() => handleSelect("Mild")}
            className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
          >
            <span>Mild</span>
          </DropdownMenuItem>
          <DropdownMenuItem
            onClick={() => handleSelect("Clear")}
            className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
          >
            <span>Clear</span>
          </DropdownMenuItem>
          <DropdownMenuItem
            onClick={() => handleSelect("Fog")}
            className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
          >
            <span>Fog</span>
          </DropdownMenuItem>
          <DropdownMenuItem
            onClick={() => handleSelect("Hot")}
            className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
          >
            <span>Hot</span>
          </DropdownMenuItem>
          <DropdownMenuItem
            onClick={() => handleSelect("Humid")}
            className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
          >
            <span>Humid</span>
          </DropdownMenuItem>
          <DropdownMenuItem
            onClick={() => handleSelect("Heatwave")}
            className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
          >
            <span>Heatwave</span>
          </DropdownMenuItem>
          <DropdownMenuItem
            onClick={() => handleSelect("Rainy")}
            className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
          >
            <span>Rainy</span>
          </DropdownMenuItem>
          <DropdownMenuItem
            onClick={() => handleSelect("Thunderstorm")}
            className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
          >
            <span>Thunderstorm</span>
          </DropdownMenuItem>
        </DropdownMenuGroup>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
