declare module 'expect' {
    interface AsymmetricMatchers {
        toBeBoolean(floor: number, ceiling: number): void;
    }
    interface Matchers<R> {
        toBeBoolean(): R;
    }
}
export {};
