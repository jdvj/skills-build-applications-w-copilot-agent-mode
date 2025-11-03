

import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
    <h1>OctoFit Tracker</h1>
    <p>Bienvenido a la app de seguimiento fitness OctoFit.</p>
        </header>
        <nav>
          <Link to="/activities">Activities</Link>
          <Link to="/leaderboard">Leaderboard</Link>
          <Link to="/teams">Teams</Link>
          <Link to="/users">Users</Link>
          <Link to="/workouts">Workouts</Link>
        </nav>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<Leaderboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
