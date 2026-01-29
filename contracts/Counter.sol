// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Counter {
    uint256 public count;
    address public owner;
    
    event CountIncremented(uint256 newCount);
    event CountDecremented(uint256 newCount);
    event CountSet(uint256 newCount);
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    
    constructor() {
        owner = msg.sender;
        count = 0;
    }
    
    function increment() public {
        count = count + 1;
        emit CountIncremented(count);
    }
    
    function decrement() public {
        require(count > 0, "Count cannot go below zero");
        unchecked {
            count = count - 1;   
        }
        emit CountDecremented(count);
    }
    
    function setCount(uint256 _count) public onlyOwner {
        require(_count <= 100, "Count too high");
        count = _count;
        emit CountSet(count);
    }
    
    function reset() public onlyOwner {
        count = 0;
    }
    
    function isAboveThreshold(uint256 threshold) public view returns (bool) {
        return count >= threshold;
    }
}