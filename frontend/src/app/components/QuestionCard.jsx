import React from "react";

function QuestionCard() {
  return (
<div className="card w-96 bg-base-100 card-sm shadow-sm">
  <div className="card-body">
    <h2 className="card-title">What is the capital city of Cyprus?</h2>
    <div className="card-actions justify-end">
      <button className="btn btn-primary">Edit</button>
    </div>
  
  </div>
</div>
  );
}

export default QuestionCard;
