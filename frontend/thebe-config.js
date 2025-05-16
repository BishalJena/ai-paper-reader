thebelab.configure({
  requestKernel: () => Promise.resolve({
    kernelOptions: { name: 'python3' }
  }),
  binderOptions: { repo: 'user/mlpaper-interact', ref: 'main' }
});
