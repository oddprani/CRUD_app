import React, { useState } from 'react';
import { motion } from 'framer-motion';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState('');
  const [editIndex, setEditIndex] = useState(null);

  const handleAddOrUpdate = () => {
    if (input.trim() === '') return;
    if (editIndex !== null) {
      const updated = [...tasks];
      updated[editIndex] = input.trim();
      setTasks(updated);
      setEditIndex(null);
    } else {
      setTasks([...tasks, input.trim()]);
    }
    setInput('');
  };

  const handleEdit = (i) => {
    setInput(tasks[i]);
    setEditIndex(i);
  };

  const handleDelete = (i) => {
    setTasks(tasks.filter((_, idx) => idx !== i));
    if (editIndex === i) {
      setInput('');
      setEditIndex(null);
    }
  };

  return (
    <div className="container">
      <h1>✨ Your Vibe List</h1>
      <div className="input-wrap">
        <input
          type="text"
          placeholder="What's the move?"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button onClick={handleAddOrUpdate}>
          {editIndex !== null ? 'Save ✏️' : 'Add ➕'}
        </button>
      </div>

      <motion.ul
        className="task-list"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.3 }}
      >
        {tasks.map((task, i) => (
          <motion.li
            key={i}
            initial={{ y: 10, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: i * 0.05 }}
          >
            <span>{task}</span>
            <div>
              <button onClick={() => handleEdit(i)}>✏️</button>
              <button onClick={() => handleDelete(i)}>🗑️</button>
            </div>
          </motion.li>
        ))}
      </motion.ul>
    </div>
  );
}

export default App;
