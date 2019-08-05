# Configuration Management

![make file](https://www.asdreports.com/media/PR_6923.jpeg)
reference([https://www.plutora.com/blog/configuration-management](https://www.plutora.com/blog/configuration-management))

Configuration management is an increasingly important foundation for a successful tech platform. Good leaders in the tech space will want to know what it takes to implement it. If that’s you, you’re in luck! In this post, we’ll discuss a few key things:

-   What configuration management is and where it originated from.
-   The benefits of configuration management.
-   How configuration management fits with concepts like  [DevOps and agile](https://www.plutora.com/blog/agile-devops-effect-6-keys-software-delivery-evolution).
-   How you can get started with configuration management.

## What Is Configuration Management?

it’s the discipline of ensuring that all software and hardware assets which a company owns are known and tracked at all times—any future changes to these assets are known and tracked. You can think of configuration management like an always up-to-date inventory for your technology assets, a single source of truth.

## Create files and folders

The file explorer is accessible using the button in left corner of the navigation bar. You can create a new file by clicking the **New file** button in the file explorer. You can also create folders by clicking the **New folder** button.

Configuration management usually spans a few areas. It often relates to different ideas, like creating “software pipelines” to build and test our software artifacts. Or it might relate to writing “infrastructure-as-code” to capture in code the current state of our infrastructure. And it could mean incorporating configuration management tools such as [Chef](https://www.plutora.com/ci-cd-tools/configuration-management-tools/chef), [Puppet](https://www.plutora.com/ci-cd-tools/configuration-management-tools/puppet-labs), and [Ansible](https://www.plutora.com/ci-cd-tools/configuration-management-tools/ansible) to store the current state of our servers.

## **What the World Looks Like With Configuration Management**

Before we explore different tools for configuration management, we need to know what end results we’ll receive for our efforts.

What are the outcomes of well-implemented configuration management?

Let’s cover the benefits.

### Benefit 1: Disaster Recovery

If the worst does happen, configuration management ensures that our assets are easily recoverable. The same applies to rollbacks. Configuration management makes it so that when we’ve put out bad code, we can go back to the state of our software  _before_  the change.

### Benefit 2: Uptime and Site Reliability

The term “site reliability” refers to how often your service is up. I’ve worked at companies where each second of downtime would cost thousands—often tens or even hundreds of thousands. Eek!

A frequent cause of downtime is bad deployments, which can be caused by differences in running production servers to test servers. With our configuration managed properly, our test environments can mimic production, so there’s less chance of a nasty surprise.

### Benefit 3: Easier Scaling

Provisioning is the act of adding more resources (usually servers) to our running application. Configuration management ensures that we know what a good state of our service is. That way, when we want to increase the number of servers that we run, it’s simply a case of clicking a button or running a script. The goal is really to make provisioning a non-event.

These are just some of the benefits of configuration management. But there are some other ones, too. You’ll experience faster onboarding of new team members, easier collaboration between teams, and extended software lifecycle of products/assets, among other benefits.

## The World Without Configuration Management

Sometimes it’s easier to grasp a concept by understanding its antithesis. What does trouble look like for configuration management, and what are we trying to avoid? Let’s take a look.

A developer implementing a feature will commonly install a few bits of software and deploy code. If things are sloppy, this developer probably makes the team and manager aware of the intention to come back later to clean it all up—that it’s simply a demonstration and will be rewritten soon.

But then the deadline starts pressing, and the task of going back through and rewriting the installation steps as a script gets pushed lower and lower in priority. Before we know it, several years have passed, and a new developer gets put on the project. That developer is now left to pick up the pieces, trying to understand what happened. It’s quite likely they aren’t even going to touch the configuration of the server. Who knows what it would do!

The above situation is precisely what configuration management helps you avoid. We don’t want to be left in the dark as a result of developers setting up software without proper documentation/traceability. Rather, we want to know the answers to questions like

-   What services are we running?
-   What state are those services in?
-   How did they get to their current state?
-   What was the purpose for the changes?

Configuration management can tell us these answers.

That hopefully paints a clearer picture of the problems that configuration management is trying to solve.
