export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-10 px-4">
      <h1 className="text-5xl font-bold">Kahoot AI</h1>

      <div className="flex flex-col items-center gap-6 w-full max-w-sm">
        <button className="btn bg-primary w-full">Create Game</button>

        <div className="divider">OR</div>

        <div className="flex flex-col gap-3 w-full">
          <input
            type="text"
            placeholder="Enter Game Code"
            className="input bg-amber-100 w-full"
          />
          <button className="btn btn-ghost w-full">Join Game</button>
        </div>
      </div>
    </div>
  );
}
