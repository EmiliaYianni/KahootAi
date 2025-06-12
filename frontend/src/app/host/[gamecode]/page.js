import React from "react";

function lobby() {
  const players = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank"]; // example players
  const showLobby = false;
  return (
    <div>
      {showLobby ? (
        <div className="min-h-screen flex flex-col items-center justify-center p-6">
          <h1 className="text-4xl font-bold mb-4">Game Title</h1>

          <div className="text-center mb-6">
            <p className="text-xl mb-2">Game Code</p>
            <div className="text-6xl font-extrabold">ABC123</div>
          </div>
          <div className="divider"></div>
          <div className="grid grid-cols-3 gap-4 w-3/4 mt-6">
            {players.map((player) => (
              <div
                key={player}
                className="card bg-base-100 shadow-md p-4 flex items-center justify-center rounded"
              >
                <span className="text-lg font-medium">{player}</span>
              </div>
            ))}
            <div className="flex flex-row justify-center">
              <button className="btn bg-success text-white w-full">
                Begin Quiz!!
              </button>
            </div>
          </div>
        </div>
      ) : (
        <div className="min-h-screen flex flex-col items-center justify-center p-6">
          <div className="text-center mb-6">
            <div className="text-6xl font-extrabold">Question here</div>
          </div>
          <div className="divider"></div>

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
        </div>
      )}
    </div>
  );
}

export default lobby;
