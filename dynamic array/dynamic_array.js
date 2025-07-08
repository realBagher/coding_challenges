class DynamicArray {
    constructor(capacity) {
        this.size = 0;
        this.capacity = capacity;
        this.arr = new Array(capacity).fill(0);
    }

    get(i) {
        return this.arr[i];
    }

    set(i, n) {
        this.arr[i] = n;
    }

    pushback(n) {
        if (this.size === this.capacity) {
            this.resize();
        }
        this.arr[this.size] = n;
        this.size++;
    }

    popback() {
        this.size--;
        return this.arr[this.size];
    }

    resize() {
        const newCapacity = this.capacity * 2;
        const newArr = new Array(newCapacity).fill(0);
        for (let i = 0; i < this.size; i++) {
            newArr[i] = this.arr[i];
        }
        this.arr = newArr;
        this.capacity = newCapacity;
    }

    getSize() {
        return this.size;
    }

    getCapacity() {
        return this.capacity;
    }
}