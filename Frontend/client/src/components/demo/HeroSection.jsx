export function HeroSection() {
  return (
    <>
      <section className="bg-gray-50">
        <div className="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
          <div className="mx-auto max-w-xl text-center">
            <h1 className="text-3xl text-gray-800 font-extrabold sm:text-5xl">
              Plan Your Journey
              <strong className="font-extrabold text-blue-500 sm:block">
                {" "}
                with Confidence{" "}
              </strong>
            </h1>

            <p className="mt-4 sm:text-xl/relaxed">
              Smart traffic solutions at your fingertips. Input your location
              and travel date to unlock real-time predictions that help you
              navigate through busy streets with ease. Our advanced analytics
              ensure you always stay one step ahead of congestion.
            </p>

            <div className="mt-8 flex flex-wrap justify-center gap-4">
              <a
                className="block w-full rounded bg-blue-700/90 px-12 py-3 text-sm font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring active:bg-blue-500 sm:w-auto shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]"
                href="#"
              >
                Get Started
              </a>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
