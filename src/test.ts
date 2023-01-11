import isFullscreen from './main';
import { expect, test } from '@jest/globals';
import type { MatcherFunction } from 'expect';

const toBeBoolean: MatcherFunction<[received: boolean]> = function (received) {
  if (typeof received == 'boolean') {
    return {
      message: () => `expected ${received} to be boolean `,
      pass: true,
    };
  } else {
    return {
      message: () => `expected ${received} to be boolean `,
      pass: false,
    };
  }
};

expect.extend({
  toBeBoolean,
});

declare module 'expect' {
  interface AsymmetricMatchers {
    toBeBoolean(floor: number, ceiling: number): void;
  }
  interface Matchers<R> {
    toBeBoolean(): R;
  }
}

test('Response is boolean', () => {
  expect(isFullscreen()).toBeBoolean();
});
