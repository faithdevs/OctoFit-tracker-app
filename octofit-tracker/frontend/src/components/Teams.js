import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://ubiquitous-guacamole-7pwpvqx5pwphx5wj-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center text-info">Teams</h1>
      <div className="card">
        <div className="card-body">
          <ul className="list-group">
            {teams.map(team => (
              <li key={team.id} className="list-group-item">
                {team.name}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Teams;