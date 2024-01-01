package main

import "fmt"

type Vector struct {
    size     int
    capacity int
    data     []int
}

func NewVector() *Vector {
    return &Vector{size: 0, capacity: 16, data: make([]int, 16)}
}

func (v *Vector) PushBack(value int) {
    if v.size == v.capacity {
        v.capacity *= 2
        new_data := make([]int, v.capacity)
        copy(new_data, v.data)
        v.data = new_data
    }
    v.data[v.size] = value
    v.size++
}

func (v *Vector) Get(index int) int {
    return v.data[index]
}

func (v *Vector) Size() int {
    return v.size
}

func main() {
    vec := NewVector()
    vec.PushBack(1)
    vec.PushBack(2)
    vec.PushBack(3)

    for i := 0; i < vec.Size(); i++ {
        fmt.Println(vec.Get(i))
    }
}
