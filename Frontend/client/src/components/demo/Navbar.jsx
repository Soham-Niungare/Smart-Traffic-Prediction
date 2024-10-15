import { DropdownMenuNav } from "./DropdownMenuNav";

export function Navbar() {
  return (
    <>
      <header className="bg-[#FF921C] border-b-4 border-black">
        <div className="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
          <div className="flex h-16 items-center justify-between">
            <div className="md:flex md:items-center md:gap-12">
              <a className="block text-gray-400" href="#">
                <span className="sr-only">Home</span>
                <h1 className="flex flex-col font-bold ">
                  <span className="text-xl text-white text-center -mb-1">
                    Traffic
                  </span>
                  <span className="text-3xl text-teal-800 -mt-1">Analysis</span>
                </h1>
              </a>
            </div>

            <div className="hidden md:block">
              <nav aria-label="Global">
                <ul className="flex items-center gap-6 text-md">
                  <li>
                    <a
                      className="text-white font-bold text-xl transition hover:text-gray-500/75"
                      href="#"
                    >
                      {" "}
                      About{" "}
                    </a>
                  </li>

                  <li>
                    <a
                      className="text-white font-bold text-xl transition hover:text-gray-500/75"
                      href="#"
                    >
                      {" "}
                      Careers{" "}
                    </a>
                  </li>

                  <li>
                    <a
                      className="text-white font-bold text-xl transition hover:text-gray-500/75"
                      href="#"
                    >
                      {" "}
                      Projects{" "}
                    </a>
                  </li>

                  <li>
                    <a
                      className="text-white font-bold text-xl transition hover:text-gray-500/75"
                      href="#"
                    >
                      {" "}
                      Blog{" "}
                    </a>
                  </li>
                </ul>
              </nav>
            </div>

            <div className="block md:hidden">
              <DropdownMenuNav></DropdownMenuNav>
            </div>
          </div>
        </div>
      </header>
    </>
  );
}
