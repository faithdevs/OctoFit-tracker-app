import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://ubiquitous-guacamole-7pwpvqx5pwphx5wj-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center text-danger">Workouts</h1>
      <div className="card">
        <div className="card-body">
          <ul className="list-group">
            {workouts.map(workout => (
              <li key={workout.id} className="list-group-item">
                {workout.name}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Workouts;