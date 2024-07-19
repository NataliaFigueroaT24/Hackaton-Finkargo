import React, { useState } from 'react';
import { getSupportCase } from '../api';

const TrackCaseForm: React.FC = () => {
  const [caseId, setCaseId] = useState('');
  const [caseData, setCaseData] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const result = await getSupportCase(Number(caseId));
    setCaseData(result);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Case ID</label>
          <input
            type="text"
            value={caseId}
            onChange={(e) => setCaseId(e.target.value)}
            required
          />
        </div>
        <button type="submit">Track Case</button>
      </form>
      {caseData && (
        <div>
          <h3>Case Details</h3>
          <p>Title: {caseData.title}</p>
          <p>Description: {caseData.description}</p>
          <p>Status: {caseData.status}</p>
        </div>
      )}
    </div>
  );
};

export default TrackCaseForm;
