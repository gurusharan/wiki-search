### What is this?

It's a DIY asynchronous microframework to further explore Python35+, software architecture, and a few other interesting things. It is composed of a simple HTTP/1.1 async server and the actual framework.

Here are some of the things it can do:

- [Dependency injection][1] and how it affects application design and ease of testing.
- We can use the comfortable `[asyncio.start_server][2]` interface to write asynchronous networking code.
- A naive approach to parsing HTTP requests and routing requests.
- A first try at [the Clean Architecture][3] based on Brandon Rhode's [The Clean Architecture in Python][4]The business logic constitutes parsing requests, routing requests, etc.
The IO depends on the entity and this dependency happens only one way.

Refs:

- [http://justanr.github.io/exploring-code-architecture][5] 
- [Ruby Midwest 2011 - Architecture: The Lost Years by Uncle Bob][6]
- [Ruby Conf 12 - Boundaries by Gary Bernhardt][7]
- [Refactoring Code that Accesses External Services][8]

### Running

To run the example application, just execute it with a Python3.5 interpreter:

    python application_example.py

Additional Refs:
[1]: https://en.wikipedia.org/wiki/Dependency_injection
[2]: https://docs.python.org/3/library/asyncio-stream.html
[3]: https://blog.8thlight.com/uncle-bob/2012/08/13/the-clean-architecture.html
[4]: https://www.youtube.com/watch?v=DJtef410XaM
[5]: http://justanr.github.io/exploring-code-architecture
[6]: https://www.youtube.com/watch?v=WpkDN78P884
[7]: https://www.youtube.com/watch?v=yTkzNHF6rMs
[8]: http://martinfowler.com/articles/refactoring-external-service.html
