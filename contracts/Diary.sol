// Diary.sol
pragma solidity ^0.8.0;

contract Diary {
    struct Entry {
        uint256 timestamp;
        string content;
    }

    mapping(address => Entry[]) private entries;

    function addEntry(string memory _content) public {
        entries[msg.sender].push(Entry(block.timestamp, _content));
    }

    function getEntries() public view returns (Entry[] memory) {
        return entries[msg.sender];
    }
}
