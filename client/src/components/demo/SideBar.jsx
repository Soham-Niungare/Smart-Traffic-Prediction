import { Footer } from "./Footer";

export function SideBar() {
  return (
    <>
      <div className="flex h-[100%] flex-col justify-between border-e bg-gray-800 text-gray-200 rounded-br-3xl">
        <div className="px-4 py-6">
          <span className="grid h-10 w-32 place-content-center rounded-lg bg-gray-800 text-xl font-bold text-gray-200">
            UrbanFlow
          </span>

          <ul className="mt-6 space-y-1">
            <li>
              <a
                href="#"
                className="block rounded-lg bg-gray-800 px-4 py-2 text-sm font-medium text-gray-200"
              >
                General
              </a>
            </li>

            <li>
              <a
                href="#"
                className="block rounded-lg px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-700"
              >
                About Us
              </a>
            </li>

            <li>
              <a
                href="#"
                className="block rounded-lg px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-700"
              >
                Prediction
              </a>
            </li>

            <li>
              <a
                href="#"
                className="block rounded-lg px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-700"
              >
                Contact Us
              </a>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
}
