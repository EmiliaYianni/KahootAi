"use client";
import React, { useState } from "react";
import QuestionCard from "../components/QuestionCard";

function CreateGame() {
  const [questions, setQuestions] = useState([<QuestionCard/>, <QuestionCard/>]);

  return (
    <>
      {questions.length == 0 ? (
        <div className="max-w-md mx-auto flex flex-col gap-6 p-4">
          <div className="text-lg font-medium">
            Enter a topic to generate the quiz for
          </div>
          <input
            type="text"
            placeholder="e.g. Space, Photosynthesis, History..."
            className="input input-lg input-bordered w-full"
          />

          <div>
            <p className="mb-2 font-medium">Number of questions</p>
            <div className="flex gap-4">
              <label className="flex items-center gap-2">
                <input
                  type="radio"
                  name="radio-questions"
                  className="radio radio-neutral"
                  defaultChecked
                />
                <span>5</span>
              </label>
              <label className="flex items-center gap-2">
                <input
                  type="radio"
                  name="radio-questions"
                  className="radio radio-neutral"
                />
                <span>10</span>
              </label>
              <label className="flex items-center gap-2">
                <input
                  type="radio"
                  name="radio-questions"
                  className="radio radio-neutral"
                />
                <span>15</span>
              </label>
              <label className="flex items-center gap-2">
                <input
                  type="radio"
                  name="radio-questions"
                  className="radio radio-neutral"
                />
                <span>20</span>
              </label>
            </div>
          </div>

          <button className="btn bg-primary text-white w-full">
            Generate Questions
          </button>

         
        </div>
      ) : (
        <div className="max-w-md mx-auto flex flex-col gap-6 p-4">
            <QuestionCard/>
            <QuestionCard/>
            <QuestionCard/>
            <QuestionCard/>
            <button className="btn bg-success text-white w-full">Create Lobby</button>
        </div>
      )}
    </>
  );
}

export default CreateGame;
