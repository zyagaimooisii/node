import {PythonShell} from 'python-shell';

PythonShell.run('main.py', null).then(messages=>{
  console.log('finished');
});
