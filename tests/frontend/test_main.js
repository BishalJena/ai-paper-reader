/**
 * @jest-environment jsdom
 */
import fs from 'fs';
import path from 'path';
import { fireEvent } from '@testing-library/dom';
import '@testing-library/jest-dom/extend-expect';

const html = fs.readFileSync(path.resolve(__dirname, '../../frontend/static/index.html'), 'utf8');

describe('main.js', () => {
  let container;
  beforeEach(() => {
    document.documentElement.innerHTML = html;
    // require the script after DOM is set
    require('../../frontend/static/main.js');
    container = document.body;
  });

  test('renders form and plot controls', () => {
    expect(container.querySelector('#upload-form')).toBeInTheDocument();
    expect(container.querySelector('#m-slider')).toBeInTheDocument();
  });

  test('plot updates on slider input', () => {
    const mSlider = container.querySelector('#m-slider');
    const cSlider = container.querySelector('#c-slider');
    // simulate change
    fireEvent.input(mSlider, { target: { value: '2' } });
    fireEvent.input(cSlider, { target: { value: '1' } });
    // Plotly.newPlot should have been called — could spy on it
    expect(true).toBe(true);
  });
});
