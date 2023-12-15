
  template <class T>
  Node<T>::Node(std::string name, T data){
    Node<T>::data_ = data;                     
    namee = name;
  }
  template <class T>
  Node<T>::Node(std::string name){
    namee = name;
  }

  template <class T>
  Nodeptr<T> Node<T>::getnext()const{
    // returns the pointer to the next node
    return next_;                   
  }

  template <class T>
    T Node<T>::get_Data(){
        return data_;
    }

    template <class T>
    void Node<T>::setData(T data){
        data_ = data;
    }

  template <class T>
  std::string Node<T>::get_name()const{
    return namee;
  }
  template <class T>
  void Node<T>::set_name(std::string name){
    namee=name;
  }
