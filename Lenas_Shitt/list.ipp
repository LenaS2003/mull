

template <class T> using Nodeptr = std::shared_ptr<Node<T>>;

  template <class T>
  List<T>::List(){
    size_ = 0;
  }

  template <class T>
  Nodeptr<T> List<T>::push(std::string name, T x){
    push_c(name, x);
    return head;
  }
  template <class T>
  Nodeptr<T> List<T>::push(std::string name){
    push_c(name);
    return head;
  }

  template <class T>
  Node<T>* List<T>::push_c(std::string name, T x){
    // create a pointer to a node with the data
    Nodeptr<T> temp = std::make_shared<Node<T>>(name,x);
    // we need to update some pointers
    temp->next_ = head;
    head = temp;

    size_++;

    return head.get();
  }
  template <class T>
  Node<T>* List<T>::push_c(std::string name){
    // create a pointer to a node with the data
    Nodeptr<T> temp = std::make_shared<Node<T>>(name);
    // we need to update some pointers
    temp->next_ = head;
    head = temp;

    size_++;

    return head.get();
  }

  /* Only pushes an Element after current if current isn't the Nullpointer*/
  template <class T>
  Nodeptr<T> List<T>::push_after(const Nodeptr<T>& current, std::string name,  T x){
    //we need to make sure, that we can push an element after another
    if (current == nullptr){ 
          std::cout << "a null pointer was passed." << std::endl; 
      
      return nullptr;
    }
    else{
      // create a pointer to a node with the data
      Nodeptr<T> temp = std::make_shared<Node<T>>(name,x);
      // we need to update some pointers
      temp->next_ = current->getnext();
      current->next_ = temp;

      size_++;
      return temp;
    }
  }
    /* Only pushes an Element after current if current isn't the Nullpointer*/
  template <class T>
  Nodeptr<T> List<T>::push_after(const Nodeptr<T>& current, std::string name){
    //we need to make sure, that we can push an element after another
    if (current == nullptr){
          std::cout << "a null pointer was passed." << std::endl; 
    }
    else{
      // create a pointer to a node with the data
      Nodeptr<T> temp = std::make_shared<Node<T>>(name);
      // we need to update some pointers
      temp->next_ = current->getnext();
      current->next_ = temp;

      size_++;
    }

    return current;
  }

  template <class T>
  Node<T>* List<T>::pop_c(){
    //we need to make sure, that we can pop an element
    if (head == nullptr){  
            throw(1);    
            return nullptr;
        }
    else{
      // we need to update some pointers
      head = head->getnext();

      size_--;
    }
    return head.get();
  }

  template <class T>
  Nodeptr<T> List<T>::pop(){
    //we need to make sure, that we can pop an element
    try { 
            pop_c();
            
        }                 
        catch (int i){ 
            std::cout << " no element can be removed because the list is empty" << std::endl; 
            return nullptr;
        }
    return head;
  }

  /*  Only removes an Element after current if current isn't the Nullpointer*/
  template <class T>
  Nodeptr<T> List<T>::pop_after(const Nodeptr<T>& current){
    //we need to make sure, that we can pop an element
  
    if (head == nullptr){        
      std::cout << " no element can be removed because the list is empty" << std::endl; 
    } 

    //we need to make sure the input is valid
    else if (current == nullptr){            
      std::cout << "a null pointer was passed." << std::endl;
    } else if(current->getnext() != nullptr){
      //need to update some pointers
      current->next_ = current->getnext()->getnext();
      size_--;
    }
    return current;
  }

  template <class T>
  Nodeptr<T> List<T>::next(const Nodeptr<T>& current) const{
    // need to check if the input was valid
    if (current == nullptr){        
      std::cout << "a null pointer was passed." << std::endl;
      return nullptr;
    }

    return current->getnext();
  }

  template <class T>
  void List<T>::print() const{
    // need to check if we can print the list
    if (head == nullptr){            
      std::cout << "the list can't be printed because the list is empty" << std::endl;
      return; 
    }
    // we go through the list startig with the head
    Nodeptr<T> temp = head;
    while(temp != nullptr){
      // whe print the name and data of the node
      std::cout << temp->get_name() << ", " <<temp->get_Data() << "\n";
      //get the next node
      temp = temp->getnext();
    }
    std::cout << std::endl;
  }
    
  template<class T>
  int List<T>::size()const{
    return size_;
  }

  template<class T>
  bool List<T>::is_last(const Nodeptr<T>& current){
    // need to check if the input was valid
    if (current == nullptr){        
      
      std::cout << "a null pointer was passed." << std::endl; 
    }

    // need to check if there is an last element
    else if (head == nullptr){          
      std::cout << "there is no last element because the list is empty" << std::endl; 
    }

    else if(current->getnext() == nullptr){
      return true;
    }
    return false;
  }

  template <class T>
  Nodeptr<T> List<T>::first() const{
    return head;
  }


  /***************************************************************************
   * deletes the first Element with value if such one exist.
   * This Works in 3 Steps:
   *    1)  We check if the head is already the first Node with the given value.
   *        if it is we use the function pop and return the head. If this isn't
   *        the case we go to Step 2.
   *    2)  We declare a new variable temp and give it the head. As long as the
   *        following Node doesn't have the the given Value [and exists] we set
   *        temp on the next Node.
   *    3)  Now the next node is the Nullpointer or a node with the given Value.
   *        However now we can use the Function pop_after on temp, return temp
   *        and are Done
  ***************************************************************************/
  template <class T>
  Nodeptr<T> List<T>::erase(const std::string &value){
    // need to check if we can remove an element
    if (head == nullptr){  
      std::cout << " no element can be removed because the list is empty" << std::endl; 
      return nullptr;
    }

    else if(head->get_name() == value){
      // the first element is the one we want to remove
      // so we can just use the pop() function
      pop();
      return head;
    }
    else{
      // need to look for the element in the list
      Nodeptr<T> temp = head;
      while(temp != nullptr && temp->getnext() != nullptr && temp->getnext()->get_name() != value){
        temp = temp->getnext();

        //if the next one is the nullptr then there is no such element in the list
        if (temp->getnext() == nullptr){
          std::cout << "There is no element " << value << " in the list" << std::endl;
          return nullptr;
        }
      }
      //now that we have determined the pointer, pointing to the node, we can remove that node with pop_after
      pop_after(temp);
      return temp;
    }
  }

  template <class T>
  bool List<T>::is_in(std::string name) const{
    // our return value
    bool rt = false;
    // we go through the list starting with the head
    Nodeptr<T> ptr = head;
    while (!rt && ptr!=nullptr){

      if(ptr->get_name()==name){
        //if that is name, than we have found our node and we can return true
        rt = true;
      }
      ptr = ptr->next_;
    }
    return rt;
  }



