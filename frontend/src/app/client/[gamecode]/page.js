import React from "react";

function page() {
  const showLoadingScreen = false;
  return (
    <div>
      {showLoadingScreen ? (
        <div className="min-h-screen flex flex-col items-center justify-center bg-base-200 text-center">
          <h1 className="text-4xl font-bold mb-6">You're in!</h1>
          <span className="loading loading-dots loading-lg text-primary"></span>
        </div>
      ) : (
        <div className="grid grid-cols-2 grid-rows-2 w-screen h-screen px-10 py-10">
          <div className="flex items-center justify-center bg-primary text-white text-xl font-bold">
            Answer 1
          </div>
          <div className="flex items-center justify-center bg-secondary text-white text-xl font-bold">
            Answer 2
          </div>
          <div className="flex items-center justify-center bg-accent text-white text-xl font-bold">
            Answer 3
          </div>
          <div className="flex items-center justify-center bg-neutral text-white text-xl font-bold">
            Answer 4
          </div>
        </div>
      )}
    </div>
  );
}

export default page;
