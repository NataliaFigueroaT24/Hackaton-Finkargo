import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CreateCaseForm from './components/CreateCaseForm';
import TrackCaseForm from './components/TrackCaseForm';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/create-case" element={<CreateCaseForm />} />
        <Route path="/track-case" element={<TrackCaseForm />} />
      </Routes>
    </Router>
  );
};

export default App;


