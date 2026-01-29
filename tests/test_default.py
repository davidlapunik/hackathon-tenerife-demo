from wake.testing import *
from pytypes.contracts.Counter import Counter


@default_chain.connect()
def test_increment():
    owner = default_chain.accounts[0]
    counter = Counter.deploy(from_=owner)
    
    assert counter.count() == 0
    counter.increment(from_=owner)
    assert counter.count() == 1
    counter.increment(from_=owner)
    assert counter.count() == 2


@default_chain.connect()
def test_decrement():
    owner = default_chain.accounts[0]
    counter = Counter.deploy(from_=owner)
    
    counter.increment(from_=owner)
    counter.increment(from_=owner)
    assert counter.count() == 2
    
    counter.decrement(from_=owner)
    assert counter.count() == 1


@default_chain.connect()
def test_decrement_reverts_at_zero():
    owner = default_chain.accounts[0]
    counter = Counter.deploy(from_=owner)
    
    assert counter.count() == 0
    
    with must_revert():
        counter.decrement(from_=owner)


@default_chain.connect()
def test_set_count():
    owner = default_chain.accounts[0]
    counter = Counter.deploy(from_=owner)
    
    counter.setCount(50, from_=owner)
    assert counter.count() == 50


@default_chain.connect() 
def test_set_count_reverts_if_too_high():
    owner = default_chain.accounts[0]
    counter = Counter.deploy(from_=owner)
    
    with must_revert():
        counter.setCount(101, from_=owner)


@default_chain.connect()
def test_only_owner_can_set():
    owner = default_chain.accounts[0]
    attacker = default_chain.accounts[1]
    counter = Counter.deploy(from_=owner)
    
    with must_revert():
        counter.setCount(10, from_=attacker)


@default_chain.connect()
def test_reset():
    owner = default_chain.accounts[0]
    counter = Counter.deploy(from_=owner)
    
    counter.increment(from_=owner)
    counter.increment(from_=owner)
    assert counter.count() == 2
    
    counter.reset(from_=owner)
    assert counter.count() == 0


@default_chain.connect()
def test_is_above_threshold():
    owner = default_chain.accounts[0]
    counter = Counter.deploy(from_=owner)
    
    counter.setCount(10, from_=owner)
    assert counter.isAboveThreshold(5) == True