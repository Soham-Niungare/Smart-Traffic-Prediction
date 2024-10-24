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

export function DropdownMenuLoc({ roadNames, onLocationChange }) {
  const handleSelect = (roadName) => {
    onLocationChange(roadName);
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
          {roadNames.map((roadName, index) => (
            <DropdownMenuItem
              key={`${roadName}-${index}`}
              onClick={() => handleSelect(roadName)}
              className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
            >
              <span>{roadName}</span>
            </DropdownMenuItem>
          ))}
        </DropdownMenuGroup>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
