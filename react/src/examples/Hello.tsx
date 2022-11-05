import React from "react";
import PropTypes from "prop-types";

/**
 * React TypeScript Example
 */
export default function Hello({ name }: { name: string }) {
  return <p>Hello, {name}!</p>;
}

Hello.propTypes = {
  name: PropTypes.string.isRequired
};
